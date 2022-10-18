class Cmd:

    def GetNumber(label,min=-float('inf'),max=float('inf')):
        num = input(label)
        try:
            num = float(num)

            if num < min :
                print('The value entered is less than the minimum allowed.')
                return Cmd.GetNumber(label,min,max)

            if num > max :
                print('The value entered is greater than the maximum allowed.')
                return Cmd.GetNumber(label,min,max)

            return num
        except ValueError:
            print('The provided value is not a number.')
            return Cmd.GetNumber(label,min,max)

    def GetString(label):
        return input(label)