require 'sinatra'
require 'sqlite3'

set :bind, "0.0.0.0"
set :port, 4444
set :environment, "production"

DBNAME = "sqli.db"

get '/' do
  erb :login
end

post '/' do
  db = SQLite3::Database.new DBNAME
  username = params[:username]
  password = params[:password]
  
  begin
    row = db.execute("select * from users where username = '%s' and password = '%s'" % [username, password])
  rescue SQLite3::SQLException => ex
    return "SQLite3::SQLException: #{ex.message}"
  rescue Exception => ex
    return "error"
  end

  if row.empty?
    erb :login
  else
    erb :flag
  end
end
