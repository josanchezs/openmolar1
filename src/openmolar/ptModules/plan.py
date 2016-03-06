#! /usr/bin/python

# ########################################################################### #
# #                                                                         # #
# # Copyright (c) 2009-2016 Neil Wallace <neil@openmolar.com>               # #
# #                                                                         # #
# # This file is part of OpenMolar.                                         # #
# #                                                                         # #
# # OpenMolar is free software: you can redistribute it and/or modify       # #
# # it under the terms of the GNU General Public License as published by    # #
# # the Free Software Foundation, either version 3 of the License, or       # #
# # (at your option) any later version.                                     # #
# #                                                                         # #
# # OpenMolar is distributed in the hope that it will be useful,            # #
# # but WITHOUT ANY WARRANTY; without even the implied warranty of          # #
# # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the           # #
# # GNU General Public License for more details.                            # #
# #                                                                         # #
# # You should have received a copy of the GNU General Public License       # #
# # along with OpenMolar.  If not, see <http://www.gnu.org/licenses/>.      # #
# #                                                                         # #
# ########################################################################### #

import logging
import re
import sys

from openmolar.settings import localsettings

LOGGER = logging.getLogger("openmolar")

treatmentTypeHeaders = {
    "Diagnosis": ("Exam", "xray", "Diagnosis", "Preventive"),
    "Perio": ("perio", ),
    "Tooth": ("UL", "LL", "UR", "LR", "Conservation"),
    "Prosthetics": ("ndu", "nld", "odu", "odl", "Prosthetics"),
    "Other": ("other", "Surgical", "Occasional",),
    "Orthodontics": ("Orthodontics",),
    "Child Specific": ("Capitation",),
    "Custom": ("custom",)}

templist = []
for quad in ("ur", "ul", "ll", "lr"):
    for tooth in range(1, 9):
        templist.append("%s%d" % (quad, tooth))

tup_toothAtts = tuple(templist)

tup_Atts = (
    'xray',
    'perio',
    'anaes',
    'other',
    'ndu',
    'ndl',
    'odu',
    'odl',
    'custom')


def plannedItems(pt):
    plannedList = []
    if pt.treatment_course.examt != "" and not pt.treatment_course.examd:
        plannedList.append(("Exam", pt.treatment_course.examt),)
    for attrib in tup_Atts + tup_toothAtts:
        tx = pt.treatment_course.__dict__[attrib + "pl"]
        if tx not in ("", None):
            items = tx.strip(" ").split(" ")
            for item in set(items):
                if item == "":
                    continue
                n = items.count(item)
                if n != 1:
                    item = "%d%s" % (n, item)
                if re.match("[ul][lr][1-8]", attrib):
                    # check for deciduous
                    toothName = str(pt.chartgrid.get(attrib)).upper()
                    plannedList.append((toothName, item),)
                else:
                    plannedList.append((attrib, item), )
    return plannedList


def completedItems(pt, teethOnly=False):
    compList = []
    if teethOnly:
        for tooth in tup_toothAtts:
            tx = pt.treatment_course.__dict__[tooth + "cmp"]
            if tx not in ("", None):
                items = tx.strip(" ").split(" ")
                for item in items:
                    if item == "":
                        continue
                    if re.match("[ul][lr][1-8]", tooth):
                        compList.append((tooth, item),)
    else:
        if pt.treatment_course.examt != "" and pt.treatment_course.examd:
            compList.append(("Exam", pt.treatment_course.examt),)

        for attrib in tup_Atts + tup_toothAtts:
            tx = pt.treatment_course.__dict__[attrib + "cmp"]
            if tx not in ("", None):
                items = tx.strip(" ").split(" ")
                for item in set(items):
                    if item == "":
                        continue
                    n = items.count(item)
                    if n != 1:
                        item = "%d%s" % (n, item)
                    if re.match("[ul][lr][1-8]", attrib):
                        # check for deciduous
                        toothName = str(pt.chartgrid.get(attrib)).upper()
                        compList.append((toothName, item),)
                    else:
                        compList.append((attrib, item), )
    return compList


def summary(pt):
    '''
    returns html set showing a summary of planned or completed treatment
    '''

    if pt.treatment_course is None or pt.treatment_course.accd is None:
        return ""

    retarg = '''<html><head>
    <link rel="stylesheet" href="%s" type="text/css">
    </head>\n<body>''' % localsettings.stylesheet

    if not pt.underTreatment:
        retarg += "<H4>%s</H4>" % _("Previous Course")
    if pt.treatment_course.accd is not None:
        retarg += '%s %s<br />' % (
            _("Start"),
            localsettings.formatDate(pt.treatment_course.accd))
        if pt.treatment_course.cmpd is not None:
            retarg += '%s %s<br />' % (
                _('End'),
                localsettings.formatDate(pt.treatment_course.cmpd))
        else:
            retarg += '<b>%s</b><br />' % _("ONGOING")

    if pt.treatment_course.ftr:
        retarg += '<font color="red">%s</font><br />' % _(
            "Patient Failed to Return")

    plan = ""
    for item in plannedItems(pt):
        plan += '%s - %s<br />' % (item)
    if plan != "":
        plan = "<h5>%s</h5>%s" % (_("PLAN"), plan)

    comp = ""
    for item in completedItems(pt):
        comp += '%s - %s<br />' % (item)
    if comp != "":
        comp = "<h5>%s</h5>%s" % (_("COMPLETED"), comp)
        if plan != "":
            plan = "<hr />" + plan

    if plan == "" and comp == "":
        return "%s%s</body></html>" % (retarg, _("No treatment"))
    else:
        return '%s%s%s</body></html>' % (retarg, plan, comp)

    return retarg


def completedFillsToStatic(pt):
    '''
    take completed items, and update the static chart
    '''
    items = completedItems(pt, teethOnly=True)
    for tooth, prop in items:
        tooth = tooth.lower()
        if re.match("EX", prop):
            pt.__dict__["%sst" % tooth] = "TM "
        elif len(prop) > 33:
            pass
        else:
            existing = pt.__dict__.get("%sst" % tooth).split(" ")
            existing.append(prop.strip(" "))
            i = 0
            correct = False
            while not correct:
                new = " ".join([s for s in existing[i:] if s != ""]) + " "
                correct = len(new) < 34
                i += 1
            pt.__dict__["%sst" % tooth] = new


def reverse_completedFillsToStatic(pt):
    '''
    undo above procedure if a course is "resumed"
    take completed items, and update the static chart
    '''
    items = completedItems(pt, teethOnly=True)
    for tooth, prop in items:
        tooth = tooth.lower()
        existing = pt.__dict__["%sst" % tooth].split(" ")
        if re.match("EX", prop):
            removal = "TM"
        else:
            removal = prop.strip(" ")
        existing.reverse()
        try:
            existing.remove(removal)
        except ValueError:
            pass  # property not found
        existing.reverse()
        new = " ".join([s for s in existing if s != ""]) + " "
        pt.__dict__["%sst" % tooth] = new


if __name__ == "__main__":
    from openmolar.dbtools import patient_class

    localsettings.initiate()
    try:
        serialno = int(sys.argv[len(sys.argv) - 1])
    except:
        serialno = 14860
    pt = patient_class.patient(serialno)
    print(plannedItems(pt))
    print(completedItems(pt))
    print(summary(pt))
