class FilterModule(object):

    def filters(self):
        return { "find_location": self.do_find_location }

    def do_find_location(self, device):
        if not device.get('tags') or not len(device.get('tags', [])) > 0:
            return "Unknown"
        return device['tags'][0].split(':')[-1]