# Daschel Cooper
import re
import sys
import math
from strint import *

RUNTIME_DEBUG = False

def clean_program(program_string):
	return re.sub(r"!.*?!|[^+\-#=><\[\]a-zA-Z0-9]","",program_string,0,re.DOTALL)
def validate_program(program_string):
	program_regex = r"(\+|\-|#[a-zA-Z0-9]+|=[a-zA-Z0-9]+|#[a-zA-Z0-9]+\[|\]|=[a-zA-Z0-9]+\[|=>|#<)*"
	match = re.fullmatch(program_regex,program_string)
	if match == None:
		return "Invalid format"
	opens = 0
	for ch in program_string:
		if ch == '[':
			opens = opens + 1
		elif ch == ']':
			opens = opens - 1
		if opens < 0:
			return "Unmatched brackets"
	if opens != 0:
		return "Unmatched brackets"
	tags = {}
	variable_instructions = re.findall(r"#[a-zA-Z0-9]+|=[a-zA-Z0-9]+|#[a-zA-Z0-9]+\[",program_string)
	for cmd in variable_instructions:
		#print(cmd)
		if cmd[0]=='#':
			tags[pull_variable(cmd)] = True
		elif cmd[0]=='=' and not pull_variable(cmd) in tags:
			return "Variable used before declaration: " + str(pull_variable(cmd))
		elif cmd[0]!='=' and not pull_variable(cmd) in tags:
			return "Variable used before declaration: " + str(pull_variable(cmd))
	return ""
def execute_program(program_string):
	commands = commandize(program_string)
	number = Strint()
	variables = {}
	run_command_section(commands,variables,number)
def commandize(program_string):
	return re.findall(r"#[a-zA-Z0-9]+\[|\]|=[a-zA-Z0-9]+\[|\+|\-|#[a-zA-Z0-9]+|=[a-zA-Z0-9]+|=>|#<",program_string)
def run_command_section(commands, variables, number):
	if RUNTIME_DEBUG: print(commands)
	INC = r"\+"
	DEC = r"\-"
	SAV = r"#[a-zA-Z0-9]+"
	ASN = r"=[a-zA-Z0-9]+"
	CLP = r"#[a-zA-Z0-9]+\["
	WLP = r"=[a-zA-Z0-9]+\["
	END = r"\]"
	INP = r"=>"
	OUT = r"#<"
	command_index = 0
	while command_index < len(commands):
		command = commands[command_index]
		if RUNTIME_DEBUG: print(command)
		if re.fullmatch(CLP,command):
			opens = 1
			endpoint = command_index + 1
			while opens > 0:
				if re.fullmatch(END,commands[endpoint]):
					opens = opens - 1
				if re.fullmatch(CLP,commands[endpoint]) or re.fullmatch(WLP,commands[endpoint]):
					opens = opens + 1
				endpoint = endpoint + 1
			counter = Strint()
			counter.set(variables[pull_variable(command)])
			while not counter.is_zero():
				if RUNTIME_DEBUG: print(counter.get())
				counter.decrement()
				variables = run_command_section(commands[command_index+1:endpoint],variables,number)
			command_index = endpoint - 1
		elif re.fullmatch(WLP,command):
			opens = 1
			endpoint = command_index + 1
			while opens > 0:
				if re.fullmatch(END,commands[endpoint]):
					opens = opens - 1
				if re.fullmatch(CLP,commands[endpoint]) or re.fullmatch(WLP,commands[endpoint]):
					opens = opens + 1
				endpoint = endpoint + 1
			while number.get() != variables[pull_variable(command)]:
				variables = run_command_section(commands[command_index+1:endpoint],variables,number)
			command_index = endpoint - 1
		elif re.fullmatch(INC,command):
			number.increment()
		elif re.fullmatch(DEC,command):
			number.decrement()
		elif re.fullmatch(SAV,command):
			variables[pull_variable(command)] = number.get()
		elif re.fullmatch(ASN,command):
			number.set(variables[pull_variable(command)])
		elif re.fullmatch(END,command):
			pass
		elif re.fullmatch(INP,command):
			number.set(program_input())
		elif re.fullmatch(OUT,command):
			print(number.get())
		else:
			print("Unrecognized command (" + command + ") - passing")


		command_index = command_index + 1
	return variables

def pull_variable(string):
	return re.findall(r"[a-zA-Z0-9]+",string)[0]
def program_input():
	string = input("Input a number:")
	while not re.fullmatch(r"0|[1-9][0-9]*",string):
		string = input("Try again:")
	return string


value = Strint()

file = open(sys.argv[1],'r')
program_string = file.read()
program_string = clean_program(program_string)
comp_error = validate_program(program_string)
if comp_error:
	print(comp_error)
	sys.exit()
execute_program(program_string)