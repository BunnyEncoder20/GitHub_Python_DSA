def caesar_cipher(str, shift)
  str.chars.map do |char|
    if not (char.ord.between?(65, 90) || char.ord.between?(97, 122))
      next char
    end
    base = 97
    base = 65 if char.ord.between?(65, 90)
    
    index = char.ord - base  # normalizing
    shifted_index = (index + shift) % 26
    (base + shifted_index).chr
  end.join
end

def better_caesar_cipher(str, shift)
  str.chars.map do |ch| 
    # 1. Guard clause: skip non letters chars
    next ch unless ch.match?(/[a-zA-Z]/)

    # 2 pick the correct base
    base = (ch == ch.upcase)? 'A'.ord : 'a'.ord

    # 3. calucale the shifted ascii and make into that char
    ((ch.ord - base + shift) % 26 + base).chr
end.join
end

puts(caesar_cipher('What a string!', 5))
puts(better_caesar_cipher('What a string!', 5))
