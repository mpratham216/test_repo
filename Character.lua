--[[
*****************************************************************************************
*
*
*  This script is code stub for CodeChef problem code WLEN_LUA
*  under contest PYLT20TS in Task 0 of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*
*  Filename:			WLEN_LUA.lua
*  Created:				07/10/2020
*  Last Modified:		07/10/2020
*  Author:				e-Yantra Team
*
*****************************************************************************************
]]--

-- countChar function to count the characters in each word of given string
a = {}
d = {}

function countChar(str)
    for word in str:gmatch("%w+") do
      d[j] = (string.format("%d",word:len()))
      j = j + 1
    end
    print(table.concat(d,","))
    d = {}
end


tc = tonumber(io.read())

if (tc >= 1 and tc <= 25) or (tc <=5 ) then
  
  for i=1,tc do
    
      str=io.read()
      a[i] = str
  end


for i=1,tc do
    j = 1
    str = a[i]
    countChar(str)
    
end

end


