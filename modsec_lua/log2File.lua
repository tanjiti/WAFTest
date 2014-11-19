--filepath setting
local filepath = '/tmp/modsec_wafLog.log'

--table to store modsecurity variables
local fileds = {}

--modsecurity lua interface function
local m_log = m.log
local m_getvar = m.getvar
local m_getvars = m.getvars
--local m_setvar = m.setvar


--lua string function
string_sub = string.sub
string_find = string.find

--lua table function
table_sort = table.sort
table_insert = table.insert

--get var through modsecurity lua inerface function getvar and getvars

local var_table = {"ARGS","ARGS_NAMES","ARGS_GET","ARGS_GET_NAMES","ARGS_POST","ARGS_POST_NAMES","FILES","FILES_NAMES","FILES_SIZES","FILES_TMPNAMES","GEO","REQUEST_COOKIES","REQUEST_COOKIES_NAMES","REQUEST_HEADERS","REQUEST_HEADERS_NAMES","RESPONSE_HEADERS","RULE","SESSION","TX","XML"}

local var_sig = {"ARGS_COMBINED_SIZE","AUTH_TYPE","DURATION","FILES_COMBINED_SIZE","HIGHEST_SEVERITY","MATCHED_VAR","MATCHED_VAR_NAME","MULTIPART_CRLF_LF_LINES","MULTIPART_STRICT_ERROR","MULTIPART_UNMATCHED_BOUNDARY","PATH_INFO","QUERY_STRING","REMOTE_ADDR","REMOTE_PORT","REMOTE_HOST","REMOTE_USER","REQBODY_PROCESSOR","REQBODY_PROCESSOR_ERROR","REQBODY_PROCESSOR_ERROR_MSG","REQUEST_BASENAME","REQUEST_BODY","REQUEST_FILENAME","REQUEST_LINE","REQUEST_METHOD","REQUEST_PROTOCOL","REQUEST_URI","REQUEST_URI_RAW","RESPONSE_BODY","RESPONSE_CONTENT_LENGTH","RESPONSE_CONTENT_TYPE","RESPONSE_PROTOCOL","RESPONSE_STATUS","SCRIPT_BASENAME","SCRIPT_FILENAME","SCRIPT_GID","SCRIPT_GROUPNAME","SCRIPT_MODE","SCRIPT_UID","SCRIPT_USERNAME","SERVER_ADDR","SERVER_NAME","SERVER_PORT","SESSIONID","TIME","TIME_DAY","TIME_EPOCH","TIME_HOUR","TIME_MIN","TIME_MON","TIME_SEC","TIME_WDAY","TIME_YEAR","URLENCODED_ERROR","USERID","WEBAPPID"}

for _,v in pairs(var_table) do
	fileds[v] = m_getvars(v)
end

for _,v in pairs(var_sig) do
	fileds[v] = m_getvar(v)
end


function main()
log(filepath,fileds)
return nil
end

function log(filepath,fileds)
  local file = assert(io.open(filepath,"w+"))

  --sort fileds
  local key_fileds = {}

  --fetch the key of fileds table
  for key,_ in pairs(fileds) do
     table_insert(key_fileds,key)
  end

  --sort the key
  table_sort(key_fileds)  
  for _,v in pairs(key_fileds) do
 
        if type(fileds[v]) == "table" then
                file:write(v,"\n")
                for _,v1 in pairs(fileds[v]) do
			local name = string_sub(v1.name,string_find(v1.name,":")+1,-1)
                        file:write("\t",name,": ",v1.value,"\n")
                end
        else
                file:write(v,": ",fileds[v],"\n")
        end
  end
   file:close()
end      



