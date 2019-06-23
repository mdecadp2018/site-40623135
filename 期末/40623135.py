import vrep
import keyboard
from time import sleep
import sys, math
# child threaded script: 
# 內建使用 port 19997 若要加入其他 port, 在  serve 端程式納入
#simExtRemoteApiStart(19999)
 
vrep.simxFinish(-1)
 
clientID = vrep.simxStart('127.0.0.1', 19997, True, True, 5000, 5)
if clientID!= -1:      
    print("Connected to remote server")
else:
    print('Connection not successful')
    sys.exit('Could not connect')



errorCode,Ball_handle=vrep.simxGetObjectHandle(clientID,'Ball',vrep.simx_opmode_oneshot_wait)
errorCode,Push_handle=vrep.simxGetObjectHandle(clientID,'Push',vrep.simx_opmode_oneshot_wait)
errorCode,RRev_handle=vrep.simxGetObjectHandle(clientID,'RRev',vrep.simx_opmode_oneshot_wait)
errorCode,LRev_handle=vrep.simxGetObjectHandle(clientID,'LRev',vrep.simx_opmode_oneshot_wait)

if errorCode == -1:
    print('Can not find left or right motor')
    sys.exit()
    
def stop():
    errorCode = vrep.simxStopSimulation(clientID,vrep.simx_opmode_oneshot_wait)
    
def start():
    errorCode = vrep.simxStartSimulation(clientID,vrep.simx_opmode_oneshot_wait)

def pause():
    errorCode = vrep.simxPauseSimulation(clientID,vrep.simx_opmode_oneshot_wait)


def play():
    KickBallV =7200
    Move_Minus =-0.1         
    Move_Plus =0.1
    L_KickBallVel = (math.pi/180)*KickBallV     
    R_KickBallVel = -(math.pi/180)*KickBallV
    pushball_vel = 100        



    while True:
        try:
            if keyboard.is_pressed('a'):
                vrep.simxSetJointTargetVelocity(clientID,LRev_handle,L_KickBallVel,vrep.simx_opmode_oneshot_wait)
            elif keyboard.is_pressed('l'):
                vrep.simxSetJointTargetVelocity(clientID,RRev_handle,R_KickBallVel,vrep.simx_opmode_oneshot_wait)
            elif keyboard.is_pressed('UP'):
                vrep.simxSetJointTargetVelocity(clientID,Push_handle,Pushball_Vel,vrep.simx_opmode_oneshot_wait)
            else:
                vrep.simxSetJointTargetVelocity(clientID,RRev_handle,L_KickBallVel,vrep.simx_opmode_oneshot_wait)
                vrep.simxSetJointTargetVelocity(clientID,LRev_handle,R_KickBallVel,vrep.simx_opmode_oneshot_wait)
                vrep.simxSetJointTargetVelocity(clientID,Push_handle,Pushball_Vel,vrep.simx_opmode_oneshot_wait)
        except:
            break
start()
play()