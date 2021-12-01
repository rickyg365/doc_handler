import os
import csv

from dataclasses import dataclass, field

"""
Program: Auto script doc creator

- Add read in from csv
"""


def read_csv(filepath="compendium.csv"):
	output = []

	with open(filepath, newline='') as csv_file:
		reader = csv.reader(csv_file)
		options = next(reader)

		for _, row in enumerate(reader):
			# options[0]
			name = row[0]

			# options[1]
			description = row[1]

			output.append(Script(name, description))

	return output


def export_str_data(data="", filepath=""):
	""" Overwrites by default """
	default_filepath = "compendium.txt"

	if filepath == "":
		filepath = default_filepath

	with open(filepath, 'w') as outbound:
		outbound.write(data)


@dataclass  # (frozen=True)
class Script:
	name: str
	description: str = "sample description"

	def __str__(self):
		return f"[ {self.name:^10} ] -> {self.description}"

	def markdown_fmt(self):
		return f"\n* __{self.name:^10}__ -> {self.description}"


class DocumentMaker:
	def __init__(self, python_list, bash_list):
		self.python = python_list
		self.bash = bash_list

		self.max_width = 52

	def __str__(self):
		new_doc = "\n--- INSERT NEW SCRIPTS HERE ---\n"

		# parse python and bash list
		new_doc += self.fmt_script_list(self.python, "PYTHON")
		new_doc += self.fmt_script_list(self.bash, "BASH")

		return new_doc

	def fmt_script_list(self, script_list, title):
		# Title
		parsed = f"\n[  {title}  ]:\n"

		# Body
		for script in script_list:
			parsed += f"\n - {script}"

		# Separator
		parsed += f"\n\n{'_' * self.max_width}\n"

		return parsed

	def make_md(self):
		new_doc = "---\n## **INSERT NEW SCRIPTS HERE**\n"

		# parse python and bash list
		new_doc += f"\n# PYTHON\n"
		for script in self.python:
			new_doc += script.markdown_fmt()

		new_doc += f"\n\n\n# BASH\n"
		for script in self.bash:
			new_doc += script.markdown_fmt()

		new_doc += "\n \n\n---"
		return new_doc


if __name__ == "__main__":
	# Given
	# python_script_list = [
	# 	Script("pyread", description="display markdown files using rich"),
	# 	Script("todo", description="Simple To Do List, run in documents")
	# ]
	#
	# bash_script_list = [
	# 	Script('scriptify', description="make a python file into a script"),
	# 	Script("linkify", description="like scriptify, but instead of moving file to bin makes a -s link")
	# ]
	# Files to read in data
	script_files = [
		"python_scripts.csv",
		"bash_scripts.csv"
	]

	# Extract Processed Data
	script_list = []

	for script_file in script_files:
		script_list.append(read_csv(script_file))

	# Use Document Handler obj to create text and markdown doc
	doc_creator = DocumentMaker(script_list[0], script_list[1])

	txt_doc = str(doc_creator)
	md_doc = doc_creator.make_md()

	print(txt_doc)
	print(md_doc)

	# base_file_name = "compendium"
	# export_str_data(txt_doc)
	# export_str_data(md_doc, f"{base_file_name}.md")
