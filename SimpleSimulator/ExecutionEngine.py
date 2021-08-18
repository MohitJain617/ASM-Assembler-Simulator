class ExecutionEngine:
	def __init__(self, memory, register):
		self.memory = memory
		self.register = register
	
	def execute(self,instr,cycle=0):
		opcode = instr[0:5]
		halted = False
		pc = 
		if(opcode == "00000"):
			#
		elif(opcode == "00001"):
			#
		elif(opcode == "00010"):
			#
		elif(opcode == "00011"):
			#
		elif(opcode == "00100"):
			self.ld(instr)
		elif(opcode == "00101"):
			self.st(instr)
		elif(opcode == "00110"):
			#
		elif(opcode == "00111"):
			#
		elif(opcode == "01000"):
			#
		elif(opcode == "01001"):
			#
		elif(opcode == "01010"):
			#
		elif(opcode == "01011"):
			#
		elif(opcode == "01100"):
			#
		elif(opcode == "01101"):
			#
		elif(opcode == "01110"):
			#
		elif(opcode == "01111"):
			if(self.jmp(instr)== True):
				pc = instr[8:16]
		elif(opcode == "10000"):
			self.jlt(instr)
		elif(opcode == "10001"):
			self.jgt(instr)
		elif(opcode == "10010"):
			self.je(instr)
		elif(opcode == "10011"):
			#
		
		return [halted,pc]
	
	def ld(self, instr):
		#binary string to integer
		reg_addr = int(instr[5:8],2)
		mem_addr = int(instr[8:16],2)
		#setting register value
		self.register.setVal(reg_addr, self.memory.getData(mem_addr))

	def st(self, instr):
		#binary string to integer
		reg_addr = int(instr[5:8],2)
		mem_addr = int(instr[8:16],2)
		#setting memory value
		self.memory.setData(mem_addr, self.register.getVal(reg_addr))
	
	def jmp(self, instr):
		return True 
		
