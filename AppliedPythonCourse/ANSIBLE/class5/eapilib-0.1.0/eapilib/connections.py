#
# Copyright (c) 2014, Arista Networks, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#   Redistributions of source code must retain the above copyright notice,
#   this list of conditions and the following disclaimer.
#
#   Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
#
#   Neither the name of Arista Networks nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL ARISTA NETWORKS
# BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN
# IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
import socket
import urlparse
import collections

import jsonrpclib

class ConnectionError(Exception):
    """ Base exception raised for connection errors
    """
    pass

class CommandError(Exception):
    """ Base exception raised for command errors
    """
    pass

class EapiConnection(object):
    """ Creates a connection for sending and receiving data using Arista
        eAPI.  In order for the API to be able to send and receive data
        the command API must be enabled in the switches running configuration.
        To enable command API execute the following configuration commands
        on the destination device:

            eos# config
            eos(config)# management api http-commands
            eos(config-mgmt-api-http-cmds)# no shutdown

        The above configuration will enable eAPI listening on the default
        HTTPS port 443.   For additional configuration options please
        consult the Arista EOS Command API Guide downloadable from
        http://www.arista.com.
    """

    def __init__(self, **kwargs):
        self.hostname = kwargs.get('hostname', 'localhost')
        self.username = kwargs.get('username', 'admin')
        self.password = kwargs.get('password', '')
        self.enable_pwd = kwargs.get('enable_password', '')

        proto = kwargs.get('protocol', 'https')
        if proto not in ['http', 'https']:
            raise ValueError('invalid protocol specified')

        port = kwargs.get('port')
        if proto == 'http' and port is None:
            port = 80
        elif proto == 'https' and port is None:
            port = 443

        if int(port) not in range(1, 65536):
            raise ValueError('port value is out of range')

        netloc = '%s:%s@%s:%s' % (self.username, self.password,
                                  self.hostname, port)
        path = '/command-api'

        self.url = urlparse.urlunsplit((proto, netloc, path, None, None))
        self.connection = jsonrpclib.Server(self.url)

    def __repr__(self):
        return 'Connection(url=%s)' % self.url

    def run_commands(self, commands, format='json'):
        """ runs the commands """

        # insert enable into the command stack
        commands.insert(0, {'cmd': 'enable', 'input': self.enable_pwd})
        resp = self.connection.runCmds(1, commands, format)

        # drop the enable command from the response
        resp.pop(0)
        return resp

    def config(self, commands):
        """ runs commands in config mode """

        if isinstance(commands, basestring):
            commands = [commands]

        if not isinstance(commands, collections.Iterable):
            raise TypeError('commands must be an interable object')

        try:
            # push the configure command onto the command stack
            commands.insert(0, 'configure')
            resp = self.enable(commands)
            resp.pop(0)

        except jsonrpclib.ProtocolError, e:
            raise CommandError(e)

        except socket.error, e:
            raise ConnectionError(e)

        return resp

    def enable(self, commands, format='json'):
        """ runs commands in enable mode """

        if isinstance(commands, basestring):
            commands = [commands]

        if not isinstance(commands, collections.Iterable):
            raise TypeError('commands must be an interable object')

        try:
            commands.insert(0, 'enable')
            resp = self.run_commands(commands, format)
            resp.pop(0)

        except jsonrpclib.ProtocolError, e:
            raise CommandError(e)

        except socket.error, e:
            raise ConnectionError(e)

        return resp

def create_connection(**kwargs):
    return EapiConnection(**kwargs)

