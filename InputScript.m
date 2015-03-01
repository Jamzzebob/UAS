%Script to imput the waypoints and other relevent data into a .txt file in
%the IMechE UAS Challenge 2015 Nottingham University team

clear
clc
format long
a= zeros(11,12); %cell array to store values
a([1:11],[12])=(1);
a([2:11],[3])=(3);

%home Location values

a([1],[2])=(1);
a([1],[4])=(16); % Waypoint type designation
lat_1=input('Homewaypoint Latitude: ');
a([1],[9])=(lat_1);
long_1=input('Homewaypoint Longitude: ');
a([1],[10])=(long_1);
sea=input('height above sea level: ');
a([1],[11])=(sea);

%Waypoint 1 - Takeoff

disp([10,'Waypoint 1 Information'])
a([2],[1])=(1);
a([2],[4])=(22); %Waypoint type designation
a([2],[5])=(input('Takeoff Pitch(deg): '));
a([2],[11])=(input('Anticipated Altitude after takeoff (m)): '));

%Waypoint 2 - Flyby Dropzone
disp([10,'Waypoint 2 information'])
a([3],[1])=(2);
a([3],[4])=(16);
brng=input('bearing angle from north (deg): ');
lat_2=asin(sin(degtorad(lat_1))*cos(0.125/6371)+cos(degtorad(lat_1))*sin(0.125/6371)*cos(degtorad(brng)));
lat_2=radtodeg(lat_2);
a([3],[9])=(lat_2);
long_2=degtorad(long_1)+atan2((sin(degtorad(brng))*sin(0.125/6371)*cos(degtorad(lat_1))),(cos(0.125/6371)-sin(degtorad(lat_1))*sin(degtorad(lat_2))));
long_2=radtodeg(long_2);
a([3],[10])=(long_2);

i=4;
while i<8;
    if i==4
        disp([10,'Dropzone information'])
    elseif i==5
        disp([10,'Waypoint A information'])
    elseif i==6
        disp([10,'Waypoint B information'])
    else 
        disp([10,'Waypoint C information'])
    end
    a([i],[1])=(i-1);
    a([i],[4])=(16); % Waypoint type designation
    a([i],[9])=(input('Latitude: '));
	a([i],[10])=(input('Longitude: '));
    a([i],[11])=(input('Altitude(m)): '));
    i=i+1;
end
    
%sets pre-landing Waypoint from home values
disp([10,'Pre-Landing waypoint'])
lat_3=asin(sin(degtorad(lat_1))*cos(0.400/6371)+cos(degtorad(lat_1))*sin(0.400/6371)*cos(degtorad(brng)));
lat_3=radtodeg(lat_3);
a([8],[9])=(lat_3);
long_3=degtorad(long_1)+atan2((sin(degtorad(brng))*sin(0.400/6371)*cos(degtorad(lat_1))),(cos(0.400/6371)-sin(degtorad(lat_1))*sin(degtorad(lat_3))));
long_3=radtodeg(long_3);
a([8],[10])=(long_3);
a([8],[11])=(input('Altitude(m)): '));

%Change speed command
disp([10,'Slow down for land information'])
a([9],[1])=(8);
a([9],[4])=(178); %Waypoint type designation
a([9],[6])=(input('Air speed (m/s): '));

%Loiter command
disp([10,'Loiter information'])
a([10],[1])=(9);
a([10],[4])=(18); %Waypoint type designation
a([10],[5])=(input('number of loops at loiter: '));
a([10],[7])=(input('loiter radius (m): '));
a([10],[11])=(input('Altitude(m)): '));

%Landing Command
disp([10,'Landing information'])
a([11],[1])=(10);
a([11],[4])=(21); %Waypoint type designation
lat_4=asin(sin(degtorad(lat_1))*cos(0.01/6371)+cos(degtorad(lat_1))*sin(0.01/6371)*cos(degtorad(brng)));
lat_4=radtodeg(lat_4);
a([11],[9])=(lat_4);
long_4=degtorad(long_1)+atan2((sin(degtorad(brng))*sin(0.01/6371)*cos(degtorad(lat_1))),(cos(0.01/6371)-sin(degtorad(lat_1))*sin(degtorad(lat_4))));
long_4=radtodeg(long_4);
a([11],[10])=(long_4);

disp(a)

b=zeros(18,2);

i=1;
bearing=0;
while i<19;
    lat_2=asin(sin(degtorad(lat_1))*cos(0.5/6371)+cos(degtorad(lat_1))*sin(0.5/6371)*cos(degtorad(bearing)));
    lat_2=radtodeg(lat_2);
    b([i],[1])=(lat_2);
    long_2=degtorad(long_1)+atan2((sin(degtorad(bearing))*sin(0.5/6371)*cos(degtorad(lat_1))),(cos(0.5/6371)-sin(degtorad(lat_1))*sin(degtorad(lat_2))));
    long_2=radtodeg(long_2);
    b([i],[2])=(long_2);
    bearing=bearing+20;
    i=i+1;
end 

disp(b)

plot(b(:,1),b(:,2),'x');

fid = fopen('Mission.txt','wt');
for ii = 1:size(a,1)
    fprintf(fid,'%g\t',a(ii,:));
    fprintf(fid,'\n');
end
fclose(fid)

fid2 = fopen('Geo.fen','wt');
for ii = 1:size(b,1)
    fprintf(fid2,'%g\t',b(ii,:));
    fprintf(fid2,'\n');
end
fclose(fid2)
