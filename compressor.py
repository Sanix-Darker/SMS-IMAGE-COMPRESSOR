import json
import binascii



GLOBAL_MAP_REPLACER = {
	"00": "1",
	"40": "2",
	"10": "3",
	"02": "4",
	"20": "5",
	"08": "6"
}

def file_to_hex(filename):
	"""
	A simple reading of a file and get the hexadecimal content

	"""
	with open(filename, 'rb') as f:
		return binascii.hexlify(f.read()).decode()


def compress(content):
	"""
	This function will compress the content with basics encoding
	rules

	- params : content
	"""
	# we initialize the pair-coccurence and the previous size of the content
	pair_occ, psize = {}, len(content)

	print("[-] Previous size :", psize)

	# basic replace of begining byte 0x
	content = content.replace(" 0x", "").replace("0x", "")

	# We loop all splitted value by taking two two elements and collect occurence numbers
	# + replacing pairs by elements in GLOBAL_MAP_REPLACER
	for c in [content[i:i+2] for i in range(0, len(content), 2)]:
		pair_occ[c] = pair_occ[c] + 1 if c in pair_occ else 1
		if c in GLOBAL_MAP_REPLACER:
			content = content.replace(c, GLOBAL_MAP_REPLACER[c])

	# we sort it
	# an print it
	print("-"*35, "\n[-] PAIRS-OCCURENCES : \n{}\n".format(
		sorted(pair_occ.items(), 
		key=lambda x: x[1], 
		reverse=True)), "-"*35)

	print("-"*35, "\n[-] COMPRESSED HEX-CONTENT : \n{}\n".format(content), "-"*35)

	# Let's print all stats
	print("[-] End size :", len(content))
	print("[-] Percentage :{}%".format((len(content)/psize)*100))
	print("[-] Removed {} characters.".format(psize - len(content)))
	print("[+] Done.")


if __name__ == "__main__":
	print("[-] SMS-FILE-COMPRESSION")

	# we ask for the input path and get it hexa content
	hex_content = file_to_hex(input("[?] file_path :"))

	print("-"*35, "\n[-] HEX-CONTENT : \n{}\n".format(hex_content), "-"*35)

	compress(hex_content)
