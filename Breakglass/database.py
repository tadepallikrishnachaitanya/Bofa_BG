#!/usr/bin/python
from django.shortcuts import render
# import MySQLdb
import pymysql
pymysql.install_as_MySQLdb()
from datetime import datetime
import datetime

DBhost = 'localhost'
DBport = 3306
DBuser = 'root'
DBpassword = 'T@depall1'
DBdatabase = 'BreakGlass'



def getApproverID(curr_user_id, request):
	db = pymysql.connect(host=DBhost, port=DBport, user=DBuser, passwd=DBpassword , db=DBdatabase, charset='utf8')
	sqlProject = 'SELECT approver_id FROM bg_user_approver_map WHERE user_id = "%s"' %curr_user_id
	print(curr_user_id);
	cursorApproverID = db.cursor()
	cursorApproverID.execute(sqlProject)
	approverID = cursorApproverID.fetchone()

	print('getApproverID')
	print(approverID)
	if approverID == None:
		return approverID
	else:
		return approverID[0]

def getUsernameByUserid(curr_user_id, request):
	db = pymysql.connect(host=DBhost, port=DBport, user=DBuser, passwd=DBpassword , db=DBdatabase, charset='utf8')
	sqlProject = 'SELECT name FROM bg_users WHERE user_id = "%s"' %curr_user_id
	print(curr_user_id)
	cursorUsername = db.cursor()
	cursorUsername.execute(sqlProject)
	usernames = cursorUsername.fetchone()
	print(usernames[0])

	return usernames[0]

def getApproverStatusByUserid(curr_user_id, request):
	db = pymysql.connect(host=DBhost, port=DBport, user=DBuser, passwd=DBpassword , db=DBdatabase, charset='utf8')
	sqlProject = 'SELECT approver FROM bg_users WHERE user_id = "%s"' %curr_user_id
	print(curr_user_id)
	cursorUserrole = db.cursor()
	cursorUserrole.execute(sqlProject)
	userrole = cursorUserrole.fetchone()
	print(userrole[0])

	return userrole[0]


def getAuditorStatusByUserid(curr_user_id, request):
	db = pymysql.connect(host=DBhost, port=DBport, user=DBuser, passwd=DBpassword , db=DBdatabase, charset='utf8')
	sqlProject = 'SELECT auditor FROM bg_users WHERE user_id = "%s"' %curr_user_id
	print(curr_user_id)
	cursorUserrole = db.cursor()
	cursorUserrole.execute(sqlProject)
	userrole = cursorUserrole.fetchone()
	print(userrole[0])

	return userrole[0]

def getRoles(request):
	db = pymysql.connect(host=DBhost, port=DBport, user=DBuser, passwd=DBpassword , db=DBdatabase, charset='utf8')
	sqlProject = 'SELECT role_id, role_name FROM bg_role' 
	cursorRoles = db.cursor()
	cursorRoles.execute(sqlProject)
	roleList = cursorRoles.fetchall()
	print(roleList)
	return roleList

def getRequestsForApproval(curr_user_id,request):
	db = pymysql.connect(host=DBhost, port=DBport, user=DBuser, passwd=DBpassword , db=DBdatabase, charset='utf8')
	# sqlProject = 'SELECT requested_by_user_id,requested_for_role_id,request_start_date_time,request_end_date_time, hours, status_comment,status FROM bg_requests WHERE approver_id = "%s"' %curr_user_id
	print('getRequestsForApproval')
	print(curr_user_id)
	sqlProject = '''SELECT
	  bg_users.name, 
	  bg_role.role_name,
	  bg_requests.request_start_date_time,
	  bg_requests.request_end_date_time,
	  bg_requests.hours,
	  bg_requests.status,
	  bg_requests.request_id,
	  bg_requests.request_created_date_time
	FROM bg_users
	JOIN bg_requests
	  ON bg_users.user_id = bg_requests.requested_by_user_id AND bg_requests.approver_id = "%s"
	  JOIN bg_role
	  ON bg_role.role_id = bg_requests.requested_for_role_id''' %curr_user_id
	cursorRequests = db.cursor()
	cursorRequests.execute(sqlProject)
	requestsList = cursorRequests.fetchall()
	
	print(requestsList)
	return requestsList

def insertRequest(request, request_id, requested_by_user_id, requested_for_role_id, approver_id, request_start_date_time, request_end_date_time, request_created_date_time,request_modified_date_time, hours):
	db = pymysql.connect(host=DBhost, port=DBport, user=DBuser, passwd=DBpassword , db=DBdatabase, charset='utf8')
	tableName = 'bg_requests'
	status = 'SUBMITTED'
	# employee_id = 2
	# conducted_date = '2017-08-29'
	# start_at = '083000'
	# end_at = '101500'
	print('view.RECEIVED REQUEST')
	print(request_start_date_time,request_end_date_time)
	print('database.insertRequest')
	print(request_id, requested_by_user_id, requested_for_role_id, approver_id, request_start_date_time, request_end_date_time, hours, request_created_date_time,status, request_modified_date_time)
	# request_start_date_time = int(request_start_date_time)
	# request_end_date_time = int(request_end_date_time)
	# request_modified_date_time = int(request_modified_date_time)
	# request_created_date_time = int(request_created_date_time)
	print('Date after INT')
	print(request_start_date_time)
	# print(datetime.utcfromtimestamp(request_start_date_time))
	# print(datetime.fromtimestamp(request_start_date_time)
	print('Date after CONVERT')
	# print(datetime.fromtimestamp(request_start_date_time/1000.0)
	# request_created_date_time = datetime.fromtimestamp(request_created_date_time/1000.0)
	# request_start_date_time = datetime.fromtimestamp(request_start_date_time/1000.0)
	# request_end_date_time = datetime.fromtimestamp(request_end_date_time/1000.0)
	# request_modified_date_time = datetime.fromtimestamp(request_modified_date_time/1000.0)
	# request_start_date_time = datetime.fromtimestamp(request_start_date_time)
	# request_end_date_time = datetime.fromtimestamp(request_end_date_time)
	# request_modified_date_time = datetime.fromtimestamp(request_modified_date_time)
	print('Date after convert')
	print(request_start_date_time)
	sqlInsertValues = ("INSERT INTO bg_requests"
					 "(request_id, requested_by_user_id, requested_for_role_id, approver_id, request_start_date_time, request_end_date_time, hours, request_created_date_time,status, request_modified_date_time)"
					 "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
	dataInsertValues = (request_id, requested_by_user_id, requested_for_role_id, approver_id, request_start_date_time, request_end_date_time, hours, request_created_date_time,status, request_modified_date_time)
	cursorInsertValues = db.cursor()
	print("sqlInsertValues")
	print(sqlInsertValues)
	# print(dataInsertValues
	cursorInsertValues.execute(sqlInsertValues,dataInsertValues)
	db.commit()
	return render(request, 'home.html')

def updateApproval(request,requestId,createdTime,responseStatus,responseStatusComment,current_user_approver_id):
	db = pymysql.connect(host=DBhost, port=DBport, user=DBuser, passwd=DBpassword , db=DBdatabase, charset='utf8')
	sqlQuery = ('UPDATE bg_requests SET status = %s, status_comment = %s WHERE request_id = %s') 
	values = (responseStatus,responseStatusComment,requestId)
	print("UPDATE REQUEST")
	print(responseStatus,requestId)
	cursorupdateApproval = db.cursor()
	cursorupdateApproval.execute(sqlQuery,values)
	db.commit();
	return render(request, 'home.html')


