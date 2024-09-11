# Copyright (C) 2024 Aadhi Kumar        
#        
# This program is free software: you can redistribute it and/or modify        
# it under the terms of the GNU Affero General Public License as published        
# by the Free Software Foundation, either version 3 of the License, or        
# (at your option) any later version.        
#        
# This program is distributed in the hope that it will be useful,        
# but WITHOUT ANY WARRANTY; without even the implied warranty of        
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the        
# GNU Affero General Public License for more details.        
#        
# You should have received a copy of the GNU Affero General Public License        
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

customers = ''    
with open('customers.txt', 'r') as f:    
    customers = f.read()    
    
payments = ''    
with open('payments.txt', 'r') as f:    
    payments = f.read()    
    
taxes = ''    
with open('taxes.txt', 'r') as f:    
    taxes = f.read()    
    
customers = customers.split('\n')    
payments = payments.split('\n')    
taxes = taxes.split('\n')    
    
for i in range(len(customers)):    
    line = ''    
        
    if type(customers[i]) == float or type(customers[i]) == int:     
        line.append(customers[i])    
    else: line+'?'            
    
    if type(payments[i]) == float or type(payments[i]) == int:     
        line.append(payments[i])    
    else: line+'\n?'
    
    if type(taxes[i]) == float or type(taxes[i]) == int:       
        line.append(taxes[i])    
    else: line+'\n?'
        
    print(line)
