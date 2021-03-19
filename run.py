
if __name__ == "__main__":
  try:
    __import__("smbf").main()
  except Exception as E:
    exit(str(E))