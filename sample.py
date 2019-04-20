import os
a=str(input("Enter a:"))#input for arg1
b=str(input("Enter b:"))#input for arg2
file1=open("clatb.v","w")#creating the tb file
file1.write('''module top;
reg [31:0]a;
reg [31:0]b;
wire [31:0]s;

cla_adder1 cla_0(a,b,s);

initial
begin
a='''+a+'''; b='''+b+''';
end

initial
begin
	$monitor("time=%3d, a=%d, b=%d, sum=%d",$time,a,b,s);
	$dumpfile("cla_adder1.vcd");
	$dumpvars;
end

endmodule
''')#writing the tb file
file1.close()#close the tb file
#make sure cla_adder1.v and clatb.v are in the same folder as this python script
os.system("iverilog -o cla cla_adder1.v clatb.v")#executing this command gives us the executable "cla"
os.system("vvp cla>result.txt")#direct the output to "result.txt" file


file=open("result.txt","r")#open "result.txt" file
print file.read();#print the contents of the file(output)
file.close()#close the file "result.txt"
