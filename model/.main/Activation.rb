ActiveRecord::Base.configurations ["development"] = > {
    "encoding" = > "utf8",
    "username" = > "",
    "adapter" = > "",
    "database" = > "",
    "host" = > "localhost",
    "password" = > "" }
        ActiveRecord::Base.connection.inspect

require ''
        conn = PG::Connection.open(:dbname => 'test')
            res = conn.exec_params('SELECT $1 AS a, $2 AS b, $3 AS c', [1, 2, nil])
require 
module FastJsonapi 
    require 'fast_jsonapi/object_serializer' 
    if defined ?(::Rails) 
        require 'fast_jsonapi/railtie' 
    elsif defined ?(::ActiveRecord) 
        require 'extensions/has_one'
    end
end
