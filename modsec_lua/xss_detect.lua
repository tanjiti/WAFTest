local string_find = string.find
local m_getvars = m.getvars
local m_log = m.log
function main()
   --Retrieve all parameters
   local get_vars = m_getvars("ARGS_GET",{"lowercase","htmlEntityDecode"});

   --Examine all variables
   for _,v in pairs(get_vars) do
	if(string_find(v.value,"<script")) then
	   --log something
           m_log(4,"Just a TEST, I'm hungry, but is 4:33 p.m ")
	   return("Suspected XSS in variable: " .. v.name .. ".")
        end
   end 

   -- Nothing wrong found.
   return nil
end
