import socket
import threading

class PortScanner(object):

   def __init__(self,hostname,s_port,f_port):
          self.hostname=hostname
          self.s_port=s_port
          self.f_port=f_port
          self.ip=socket.gethostbyname(self.hostname)

   ''' This method use python socket to connect with remote host
       on specified port. Sockettimeout is set to 1 second this
       count port close if socket not respond within this time '''
   def port_scan(self,port):
          s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
          s.settimeout(1)
          try:
             result=s.connect_ex((self.ip,port))
          except Exception as e:
             print e
          if result==0:
              print "[+] port is open %d"%port
          s.close()
   ''' Thread is spawned for each socket connection given port
       range should be in limit defined for user in operating
       system  running the script.This can be checked with `ulimit -a`'''  
   def start_scan(self):
             for port in xrange(self.s_port,self.f_port):
                 t=threading.Thread(target=self.port_scan,args=(port,))
                 t.start()

host_name=raw_input("Hostname to scan: ")
s_port=input("Initial Port:")
f_port=input("Final Port:")
p_s=PortScanner(host_name,s_port,f_port)
p_s.start_scan()
