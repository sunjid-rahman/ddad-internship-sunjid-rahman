def isPalindrome(string):
  string=string.casefold()
  if str(string) == str(string)[::-1]:
    if len(string)%2==0:
      print("Even Palindrome")
    else:
      print("Odd Palindrome")
  else:
    print("Not a Palindrome")

if __name__ == '__main__':
  string=str(input())
  isPalindrome(string)
