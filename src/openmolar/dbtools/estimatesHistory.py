# -*- coding: utf-8 -*-
# Copyright (c) 2009 Neil Wallace. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. See the GNU General Public License for more details.


from openmolar.settings import localsettings
from openmolar.connect import connect
from openmolar.ptModules import estimates

def getEsts(sno):
    db=connect()
    cursor=db.cursor()

    cursor.execute('''SELECT ix, courseno,number, itemcode, description, type,
    fee, ptfee, feescale, csetype, dent, completed, carriedover from
    estimates where serialno=%d order by ix desc'''%sno)
    rows = cursor.fetchall()
    estimatesFound=[]
    cursor.close()
    #db.close()

    for row in rows:
        #initiate a custom data class
        est=estimates.est()
        est.ix=row[0]
        est.courseno=row[1]
        est.number=row[2]
        est.itemcode=row[3]
        est.description=row[4]
        est.type=row[5]
        est.fee=row[6]
        est.ptfee=row[7]
        est.feescale=row[8]
        est.csetype=row[9]
        est.dent=row[10]
        est.completed=bool(row[11])
        est.carriedover=bool(row[12])
        estimatesFound.append(est)
        
    return estimatesFound

def details(sno):
    '''
    returns an html page showing pt's old estimates
    '''
    estimatesList=getEsts(sno)
    claimNo=len(estimatesList)
    retarg="<h2>Past Estimates - %d rows found</h2>"%claimNo
    if claimNo==0:
        return retarg
    courseno=-1
    firstRow=True
    for est in estimatesList:
        if est.courseno!=courseno:
            if not firstRow:
                retarg+="</table>"
                firstRow=False
            retarg+='''</table><h3>Estimate for course number %d</h3>
            <table width="100%%" border="1">'''% est.courseno
            retarg+=est.htmlHeader()
            courseno=est.courseno
        retarg+=est.toHtmlRow()
    retarg+='</table>\n'
    
    #db.close()
    return retarg

if __name__ == "__main__":
    localsettings.initiate()
    print'<html><body>'
    print details(707)
    print "</body></html>"