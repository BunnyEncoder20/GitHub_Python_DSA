def substrings(string, dict)
  dict.each_with_object(Hash.new(0)) do |word, result|
    matches = string.downcase.scan(word.downcase) # returns ["low", "lo"] for a word like hello
    num_of_matches = matches.length
    result[word] = num_of_matches if num_of_matches > 0
  end
end

dictionary = %w[below down go going horn how howdy it i low own part partner sit]
substrings('below', dictionary)
substrings("Howdy partner, sit down! How's it going?", dictionary)
