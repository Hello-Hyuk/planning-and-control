from math import cos, sin, tan, atan2, pi, acos, sqrt
import matplotlib.pyplot as plt

path =[[137.788742,1632.470703],[137.732239,1633.003662],[137.67514,1633.465576],[137.604904,1633.99585],[137.539551,1634.467163],[137.467392,1634.971191],[137.393951,1635.471313],[137.320557,1635.960693],[137.243561,1636.4646],[137.166565,1636.959473],[137.088623,1637.453125],[137.008896,1637.950073],[136.92778,1638.447754],[136.845886,1638.943237],[136.763535,1639.433105],[136.677719,1639.935303],[136.5914,1640.430908],[136.506241,1640.909912],[136.41272,1641.423828],[136.321671,1641.909668],[136.224869,1642.407349],[136.12381,1642.900635],[136.01265,1643.400269],[135.899597,1643.830933],[135.75795,1644.28772],[135.604584,1644.76416],[135.446747,1645.246582],[135.286514,1645.730957],[135.13179,1646.195068],[134.966431,1646.687988],[134.808105,1647.157349],[134.648666,1647.627563],[134.484207,1648.11084],[134.321732,1648.58606],[134.159836,1649.057495],[133.99588,1649.532959],[133.830811,1650.009766],[133.665344,1650.485596],[133.500275,1650.957764],[133.336243,1651.424927],[133.164886,1651.909912],[132.996887,1652.382446],[132.833206,1652.839478],[132.655334,1653.332031],[132.483994,1653.80127],[132.31514,1654.257568],[132.128403,1654.752808],[131.962097,1655.18103],[131.755295,1655.684326],[131.584869,1656.042114]]
car_len = 2 #[2m]
car_position_x = 134  
car_position_y = 1649.057495
car_vel = 20     #[m/s]
heading = 60*180/pi
Lfd = 5
Lfd_min = 5
Lfd_max = 30
r2d = 180/pi # 라디안을 deg 단위로 변환해 주는 것 2pi[rad] = 180[deg]임을 생각

if car_vel*0.3 < Lfd_min:    #look-ahead-distance를 탐색하는 범위를 min<lfd<max
    Lfd = Lfd_min            #인데, vel*0.3보다는 커야하기에 vel*0.3이 위 범위 밖이라면
elif car_vel*0.3 > Lfd_max:  # 다음과 같이 진행하도록 제어
    Lfd = Lfd_max-1
else:
    Lfd = car_vel * 0.3

for i in range(len(path)) : # 경로를 탐색하며 알고리즘 구현
    pathpoint = path[i]      # 경로에 포함된 waypoint 저장
    rel_x= pathpoint[0] - car_position_x   # 시점:차량 종점: waypoint 인 벡터 생성
    rel_y= pathpoint[1] - car_position_y
    s = sqrt(rel_x*rel_x + rel_y*rel_y)  #벡터의 크기(look-ahead-distance 거리)
    if s > Lfd_min and s < Lfd_max and s > Lfd: # 조건과 비교
        dot_x = rel_x*cos(heading) + rel_y*sin(heading) # 좌표변환
        dot_y = rel_x*sin(heading) - rel_y*cos(heading)
        if dot_x > 0 :            # 전방에 위치한 점인지 판별
            print("Look-ahead-distance : {}".format(s))
            print("waypoint : {}".format(pathpoint))
            # if dot_y > 0:                 
            #     alpha=acos(dot_x/s)   
            # else:
            #     alpha=-1*acos(dot_x/s)
            alpha =atan2(dot_y,dot_x)
            print(alpha*r2d)
            break  # 현재 시점에서 이동하기 위한 waypoint 선정완료
steering=atan2((2*car_len*sin(alpha)),s)
print("조향각[rad] : ",steering)