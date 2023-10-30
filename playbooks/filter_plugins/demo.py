class FilterModule(object):

    def filters(self):
        return { 
            "find_location": self.do_find_location,
            "new_locations": self.do_new_locations
        }

    def do_find_location(self, device):
        if not device.get('tags') or not len(device.get('tags', [])) > 0:
            return "Unknown"
        return device['tags'][0].split(':')[-1]
    
    def do_new_locations(self, locations):
        valid = []
        for loc in locations:
            try:
                import uuid
                uuid.UUID(loc)
                continue
            except ValueError:
                valid.append({
                    "type": "cmn_location",
                    "data": {
                        "name": loc
                    }
                })
        return valid