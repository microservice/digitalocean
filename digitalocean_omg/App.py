# -*- coding: utf-8 -*-
import json
import os

import click

from digitalocean import Droplet, Manager


class App:

    @click.group()
    def main():
        pass

    @main.command(name='droplet_new')
    @click.argument('name')
    @click.argument('region')
    @click.argument('size')
    @click.argument('image')
    def droplet_new(name, region, size, image):
        """
        Create a new droplet
        """
        token = os.getenv('access_token')
        kwargs = {'token': token, 'name': name, 'region': region, 'size': size,
                  'image': image}
        droplet = Droplet(**kwargs)
        droplet.create()

    @main.command()
    @click.argument('id')
    @click.argument('action')
    def droplet(id, action):
        token = os.getenv('access_token')
        droplet = Droplet(token=token, id=id)
        if action == 'status':
            droplet.load()
            click.echo(json.dumps({'status': droplet.status}))
        elif action == 'destroy':
            droplet.destroy()

    @main.command()
    @click.argument('item_type')
    def list(item_type):
        token = os.getenv('access_token')
        manager = Manager(token=token)
        if item_type == 'droplets':
            droplets = manager.get_all_droplets()
            result = []
            for droplet in droplets:
                result.append({'id': droplet.id, 'name': droplet.name, 
                               'status': droplet.status})
            click.echo(json.dumps(result))
