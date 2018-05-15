import numpy as _np
import _readconvobs
import _readsatobs
__version__ = '0.0.2'


class diag_conv(object):
    # read diag_conv file.

    def __init__(self, filename, endian='native'):
        nobs = _readconvobs.get_num_convobs(filename, endian=endian)
        self.endian = endian
        self.nobs = nobs
        self.filename = filename

    def read_obs(self):
        h_x, x_obs, x_err, x_lon, x_lat, x_press, x_time, \
            x_code, x_errorig, x_type, x_use, x_station_id, x_stnelev =\
            _readconvobs.get_convobs_data(self.filename,  self.nobs,
                                          endian=self.endian)
        self.hx = h_x
        self.obs = x_obs
        self.oberr = x_err
        self.lon = x_lon
        self.lat = x_lat
        self.press = x_press
        self.time = x_time
        self.stnelev = x_stnelev
        self.code = x_code
        self.oberr_orig = x_errorig
        self.used = x_use
        self.obtype = \
            _np.array((x_type.tostring()).replace('\x00', '')[:-1].split('|'))
        self.station_ids =\
            _np.array((x_station_id.tostring()).replace(
                '\x00', '')[:-1].split('|'))


class diag_rad(object):
    # read diag_rad file.

    def __init__(self, filename, endian='native'):
        npred, nobs = _readsatobs.get_num_satobs(filename, endian=endian)
        self.endian = endian
        self.nobs = nobs
        self.filename = filename
        self.npred = npred

    def read_obs(self):
        h_x, h_xnobc, x_obs, x_err, x_lon, x_lat, x_time, \
            x_channum, x_errorig, x_biaspred, x_use, x_qcmark,  \
            x_water_frac, x_land_frac, x_ice_frac, x_snow_frac = \
            _readsatobs.get_satobs_data(
                self.filename, self.nobs, self.npred, endian=self.endian)
        self.hx = h_x
        self.biascorr = h_x - h_xnobc
        self.obs = x_obs
        self.oberr = x_err
        self.lon = x_lon
        self.lat = x_lat
        self.time = x_time
        self.channel = x_channum
        self.biaspred = x_biaspred
        self.oberr_orig = x_errorig
        self.used = x_use
        self.qcmark = x_qcmark
        self.water_frac = x_water_frac
        self.land_frac = x_land_frac
        self.ice_frac = x_ice_frac
        self.snow_frac = x_snow_frac
