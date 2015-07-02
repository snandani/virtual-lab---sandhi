#!/usr/bin/env python
# 
# Copyright 2015 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
from gnuradio import gr

class delta_r(gr.sync_block):
    """
    docstring for block delta_r
    """
    def __init__(self,regl):
        gr.sync_block.__init__(self,
            name="delta_r",
            in_sig=[],
            out_sig=[numpy.float32])
        self._num1=regl


    def work(self, input_items, output_items):
        #in0 = input_items[0]
        delta_r = output_items[0]
        # <+signal processing here+>
        delta_r[:] = self._num1+((float)(2*self._num1)/100)
        return len(output_items[0])

