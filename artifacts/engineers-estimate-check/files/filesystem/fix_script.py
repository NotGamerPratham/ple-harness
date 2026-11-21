with open("build_memorandum.py") as f:
    code = f.read()

# Replace any multi-root parse_xml calls
code = code.replace(
    'parse_xml(f\'<w:tblHeader {nsdecls("w")}/><w:cantSplit {nsdecls("w")}/>\')',
    'parse_xml(f\'<w:tblHeader {nsdecls("w")}/>\')'
)

with open("build_memorandum.py", "w") as f:
    f.write(code)

print("Updated script.")
