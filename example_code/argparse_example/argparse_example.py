import argparse

def get_args():
  parser = argparse.ArgumentParser("This is an example of how to use arparse")
  
  ## Lets add our command line arguments here
  parser.add_argument("--argument_one", default=0, type=int,
                      help="This is the first argument")

  args = parser.parse_args()
  return args



def main():
  args = get_args()
  print(args)

  for arg in vars(args):
     print(arg, "is set to", getattr(args, arg))

  print(f"argument_one is set to {args.argument_one}")

if __name__ == '__main__':
  main()
