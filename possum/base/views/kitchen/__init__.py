# -*- coding: utf-8 -*-
#
#    Copyright 2009-2014 Sébastien Bonnegent
#
#    This file is part of POSSUM.
#
#    POSSUM is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    POSSUM is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with POSSUM.  If not, see <http://www.gnu.org/licenses/>.
#

from django.contrib import messages
from django.http import HttpResponseRedirect
import logging
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from possum.base.models import Facture
from possum.base.views import get_user


logger = logging.getLogger(__name__)


@login_required
def kitchen(request):
    data = get_user(request)
    data['menu_kitchen'] = True
    liste = []
    for bill in Facture().non_soldees():
        if bill.following.count():
            liste.append(bill)
    data['factures'] = liste
    data['need_auto_refresh'] = True
    return render_to_response('base/kitchen/home.html', data,
                              context_instance=RequestContext(request))


@login_required
def kitchen_for_bill(request, bill_id):
    data = get_user(request)
    data['menu_kitchen'] = True
    data['facture'] = get_object_or_404(Facture, pk=bill_id)
    if data['facture'].est_soldee():
        messages.add_message(request,
                             messages.ERROR,
                             "Cette facture a déjà été soldée.")
        return HttpResponseRedirect('/kitchen/')
    return render_to_response('base/kitchen/view.html', data,
                              context_instance=RequestContext(request))
