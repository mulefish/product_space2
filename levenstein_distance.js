// Function to calculate Levenshtein distance between two strings
function levenshteinDistance(str1, str2) {
    const m = str1.length;
    const n = str2.length;
    
    // Create a 2D array to store the distances
    const dp = Array(m + 1)
      .fill(null)
      .map(() => Array(n + 1).fill(null));
    
    // Initialize the first row and column of the array
    for (let i = 0; i <= m; i++) {
      dp[i][0] = i;
    }
    for (let j = 0; j <= n; j++) {
      dp[0][j] = j;
    }
    
    // Calculate the Levenshtein distance
    for (let i = 1; i <= m; i++) {
      for (let j = 1; j <= n; j++) {
        const cost = str1[i - 1] !== str2[j - 1] ? 1 : 0;
        dp[i][j] = Math.min(
          dp[i - 1][j] + 1,         // Deletion
          dp[i][j - 1] + 1,         // Insertion
          dp[i - 1][j - 1] + cost   // Substitution
        );
      }
    }
    
    // Return the Levenshtein distance
    return dp[m][n];
  }
  
const sentences = [ 
    "This is a sentence.",
    "This is a sentence.",
    "This is a cat.",
    "This is a dinosaur."

]

for ( let i = 0 ; i < sentences.length; i += 2) {
    const j = i + 1 
    const a = sentences[i]
    const b = sentences[j]
    const distance = levenshteinDistance(a, b );
    console.log(`Levenshtein distance between "${a}" and "${b}": ${distance}`);
 
}

//   // Test the Levenshtein distance function
//   const string1 = 'kitten';
//   const string2 = 'sitting';
//   const distance = levenshteinDistance(string1, string2);
  
  