input {
file {
    type => "apache"
    path => ["/etc/httpd/logs/*_log","/var/log/nginx/*.log"]
}
file {
    type => "syslog"
    path => [ "/var/log/messages", "/var/log/syslog" ]
}
file {

type => "nova"
    path => [ "/var/log/nova/*.log" ]
}
file {
    type => "cinder"
    path => [ "/var/log/cinder/*.log" ]
}
file {
    type => "neutron"
    path => [ "/var/log/neutron/*.log" ]
}
file {
    type => "ceilometer"
    path => [ "/var/log/ceilometer/*.log" ]
}
}
filter {
if [type] == "syslog" {
    grok {
      match => { "message" => "%{SYSLOGTIMESTAMP:syslog_timestamp} %{SYSLOGHOST:syslog_hostname} %{DATA:syslog_program}(?:\[%{POSINT:syslog_pid}\])?: %{GREEDYDATA:syslog_message}" }
      add_field => [ "received_at", "%{@timestamp}" ]
      add_field => [ "received_from", "%{host}" ]
    }
    syslog_pri { }
    date {
      match => [ "syslog_timestamp", "MMM  d HH:mm:ss", "MMM dd HH:mm:ss" ]
    }
  }else if [type] == "apache"  {
                if [path] =~ "access" {
                        mutate { replace => { loglevel => "apache_access" } }
                        grok {
                                match => { "message" => "%{COMBINEDAPACHELOG}" }
                                }
                        date {
                                match => [ "timestamp" , "dd/MMM/yyyy:HH:mm:ss Z" ]
        }
 } else if [path] =~ "error" {
                mutate { replace => { loglevel  => "apache_error" } }
                } else {
                        mutate { replace => { loglevel => "apache_random_logs" } }
}
}else {
        grok {
            match => ["message","%{TIMESTAMP_ISO8601:logtime} %{NUMBER:pid} %{WORD:loglevel} %{DATA:process} %{GREEDYDATA:other}"]
    }
  }
}
output {
        stdout { codec => rubydebug }
        elasticsearch_http {
                host => "192.168.215.101"
                port => "9200"
        }
}



input{
    file{
        path =>"/var/log/messages"
        start_position=>"beginning"
    }
}


output {
        elasticsearch_http {
                host => "192.168.43.212"
                port => "9200"
        }
}