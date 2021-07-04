if ARGV.count != 2
  puts "[-] Usage: #{__FILE__} <flag_file> <output_encoded_file_path>"
  exit 1;
end

fibo = Enumerator.new do|y|
  a = 0;
  b = 1
  loop {
    a, b = b, a + b;
    y << a;
  }
end

lookup = [36, 221, 193, 137, 10, 207, 131, 226, 198, 253, 127, 70, 68, 37, 157, 46, 39, 32, 184, 225, 53, 57, 51, 177, 144, 200, 48, 169, 152, 117, 115, 234, 248, 54, 64, 35, 164, 41, 105, 93, 21, 145, 196, 11, 228, 172, 55, 149, 60, 99, 82, 133, 224, 30, 243, 255, 130, 132, 181, 187, 151, 146, 150, 18, 142, 74, 214, 73, 122, 155, 139, 52, 12, 143, 213, 239, 44, 90, 58, 202, 197, 110, 160, 103, 13, 140, 31, 245, 7, 29, 91, 79, 159, 171, 5, 166, 129, 83, 63, 251, 246, 236, 15, 78, 66, 156, 8, 107, 186, 242, 75, 95, 25, 20, 84, 194, 76, 28, 92, 113, 254, 162, 161, 27, 3, 216, 100, 17, 38, 109, 14, 24, 203, 112, 235, 81, 98, 104, 45, 67, 89, 1, 0, 119, 88, 170, 189, 230, 49, 238, 135, 223, 26, 47, 85, 182, 240, 106, 80, 50, 101, 6, 180, 118, 217, 34, 108, 190, 232, 165, 154, 111, 72, 87, 201, 4, 249, 205, 212, 219, 33, 233, 43, 174, 222, 124, 123, 69, 244, 192, 9, 121, 147, 250, 229, 77, 163, 206, 191, 179, 125, 86, 59, 148, 176, 134, 97, 158, 227, 252, 208, 138, 42, 102, 128, 183, 218, 247, 22, 199, 56, 167, 195, 211, 209, 94, 71, 141, 168, 16, 65, 220, 96, 136, 120, 61, 237, 188, 62, 241, 173, 175, 114, 23, 2, 126, 215, 185, 153, 40, 116, 204, 178, 231, 210, 19]
inv_lookup = 256.times.map{|i| lookup.index(i) }

fun3 = -> c { lookup[c] ^ fibo.next }

bytes = [ ]
File.open(ARGV[0], 'rb'){|r|
  File.open(ARGV[1], 'wb') {|w|
    loop{
      chr = r.read(1)
      break if chr == nil
      bytes << fun3.(chr.ord).&(0xff)
    }
    w.puts(bytes.map{|b| '0x'+b.to_s(16).rjust(2,?0)}.join(', '))
  }
}
