from .data.defaults import DEFAULTS
from .data.bitflags import FIELD_INDEX

class SmartMixin:
    def _get_bitflag(self, field):
        return FIELD_INDEX[field]['flag']

    def _get_smart_fields(self, endpoint, scope=None):
        smart_params = {}
        for group in DEFAULTS[endpoint][scope]['Fields']:
            bit_field = 0
            for field in DEFAULTS[endpoint][scope]['Fields'][group]:
                bit_field = bit_field | self._get_bitflag(field)
            smart_params[group] = bit_field
        return smart_params
    