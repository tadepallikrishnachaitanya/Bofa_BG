from Breakglass.database import getUsernameByUserid, getRoles, insertRequest, getApproverID, getRequestsForApproval, getApproverStatusByUserid,getAuditorStatusByUserid,updateApproval
from django.shortcuts import render
from django.http import HttpResponseRedirect
import hashlib
import uuid
import time;
from django.contrib import messages
import re
# from django.shortcuts import render_to_response
import datetime
import itertools
import json
# from django.shortcuts import render_to_response
from django.http import HttpResponse

import logging



def login(request):
    request.session['current_user_id'] = '10002'
    current_user_id = request.session['current_user_id'];
    username = getUsernameByUserid(current_user_id, request)
    print ('login requests');
    print (username)
    request.session['current_username'] = username;
    current_user_id = request.session['current_user_id'];
    approver = getApproverStatusByUserid(current_user_id,request);
    auditor = getAuditorStatusByUserid(current_user_id,request);
    if approver == 1:
        print ('login YES')
        approverStatus = 'yes'
    else:
        print ('login NO')
        approverStatus = 'no'
        # return render(request,'home.html',{'approverStatus': approverStatus})
    if auditor == 1:
        print ('login YES')
        auditorStatus = 'yes'
        # return render(request,'home.html',{'auditorStatus': auditorStatus})
    else:
        print ('login YES')
        auditorStatus = 'no'
        # return render(request,'home.html',{'auditorStatus': auditorStatus}
    return render(request,'home.html',{'approverStatus': approverStatus,'auditorStatus': auditorStatus})        

def resourcerequest(request):
    roleList = getRoles(request)
    return render(request,'request.html', {'roleList': roleList})


def approverequest(request):
    current_user_id = request.session['current_user_id'];
    approver = getApproverStatusByUserid(current_user_id,request);
    if approver == 1:
        approverStatus = 'yes'
        print ('yes')
        print (current_user_id)
        approver_id = getApproverID(current_user_id, request)
        if approver_id != None:
            approver_id = approver_id.encode('UTF8')
    else:
        approverStatus = 'no'
    requestList = getRequestsForApproval(current_user_id, request);
    request_List = []
    for list in requestList:
        print (list)
        request_List.append(list)
    print ('request_List')
    print (request_List)

    # expected_output = {}
    # approve_key_data = ['RequestedBy', 'Role', 'StartTime','EndTime','Hours','Status','Action']
    # # #print StudentName_data

    # for idx, stu_id in enumerate(request_List):

    # # Loop through employee keys
    #     for key in approve_key_data:

    #     # # Form the expected json data

    #     # Check if emp_id exist in expected output
    #         if not expected_output.has_key(stu_id):
    #             expected_output[stu_id] = {}

    #         data_list = eval(key+'_data')
    #         #print data_list
    #         expected_output[stu_id][key] = data_list[idx]       

    return render(request,'approve.html',{'requestList':request_List})



def audit(request):
    current_user_id = request.session['current_user_id'];
    approver = getApproverStatusByUserid(current_user_id,request);
    if approver == 1:
        approverStatus = 'yes'
        print ('yes')
        print (current_user_id)
        approver_id = getApproverID(current_user_id, request)
        if approver_id != None:
            approver_id = approver_id.encode('UTF8')
    else:
        approverStatus = 'no'
    requestList = getRequestsForApproval(current_user_id, request);
    request_List = []
    for list in requestList:
        print (list)
        request_List.append(list)
    print ('request_List')        
    print (request_List)
    return render(request,'audit.html',{'requestList':request_List})


def submitRequest(request):
    startTimeStamp = request.POST['start-time']
    endTimeStamp = request.POST['end-time']
    hours = request.POST['hours']
    createdTimeStamp = request.POST['created-time']
    requestedRoleID = request.POST['requested-role']
    print ('view.RECEIVED REQUEST')
    print (startTimeStamp,endTimeStamp)
    startTimeStamp = startTimeStamp.encode('UTF8')
    endTimeStamp = endTimeStamp.encode('UTF8')
    createdTimeStamp = createdTimeStamp.encode('UTF8')
    requestedRoleID = requestedRoleID.encode('UTF8')
    print ('view.AFTER UTF')
    print (startTimeStamp,endTimeStamp)
    current_user_id = request.session['current_user_id'];
    gmt = time.gmtime()
    request_created_date_time = time.time()
    request_created_date_time = str(request_created_date_time).split('.')[0]
    uid = uuid.uuid4();
    uid = uid.hex
    current_user_id = current_user_id.encode('UTF8')
    current_user_id = current_user_id.decode()
    # str_object.
    approver_id = getApproverID(current_user_id, request)
    approver_id = approver_id.encode('UTF8')
    print (approver_id)
    print ('view.submitRequest')
    print (uid,current_user_id,requestedRoleID, approver_id, startTimeStamp,endTimeStamp,createdTimeStamp,createdTimeStamp,hours)
    insertRequest(request,uid,current_user_id,requestedRoleID, approver_id, startTimeStamp,endTimeStamp,createdTimeStamp,createdTimeStamp,hours)
    return render(request,'home.html')


def requestResponse(request):
    requestId = request.POST['request-id']
    createdTime = request.POST['created-time']
    responseStatus = request.POST['response-status']
    responseStatusComment = request.POST['response-status-comment']
    current_user_approver_id = request.session['current_user_id'];
    print ('view.requestResponse')
    requestId = requestId.encode('UTF8')
    responseStatus = responseStatus.encode('UTF8')
    responseStatusComment = responseStatusComment.encode('UTF8')
    print (requestId,createdTime,responseStatus,responseStatusComment,current_user_approver_id)
    updateApproval(request,requestId,createdTime,responseStatus,responseStatusComment,current_user_approver_id)
    return render(request,'home.html')


