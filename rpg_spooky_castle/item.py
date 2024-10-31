"""
The blueprint for an item.
"""

class Item:
    def __init__(self):
        self._name = None
        self._description = None

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def get_description(self):
        return self._description

    def set_description(self, value):
        self._description = value

    def describe(self):
        print("[{}] can be found here.".format(self._name))
        print(self._description)

    def __eq__(self, obj):
        try:
            if self._name == obj._name:
                return True
            else:
                return False
        except AttributeError:
            return False

#     @property
#     def name(self):
#         return self._name if isinstance(self._name, str) else str(self._name)

#     @name.setter
#     def name(self, value):
#         self._name = value

#     @property
#     def description(self):
#         return (
#             self._description
#             if isinstance(self._description, str)
#             else str(self._description)
#         )

#     @description.setter
#     def description(self, value):
#         self._description = value

