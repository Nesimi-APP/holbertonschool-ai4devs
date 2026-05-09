const users = [
    { id: 1, name: "Alice", profile: { bio: "Developer" } },
    { id: 2, name: "Bob", profile: null }, // Profile null-dur
    { id: 3, name: "Charlie" } // Profile ümumiyyətlə yoxdur
];

function displayUserBios(userList) {
    console.log("Listing User Bios...");
    
    userList.forEach(user => {
        // DÜZƏLİŞ: 
        // user.profile?.bio -> Əgər profile yoxdursa, dayanma, undefined qaytar.
        // ?? "No bio available" -> Əgər sol tərəf null/undefined olarsa, bu mesajı mənimsət.
        const bioText = user.profile?.bio ?? "No bio available";
        
        console.log(`User ID: ${user.id}`);
        console.log(`Name: ${user.name}`);
        console.log(`Bio: ${bioText}`);
        console.log("------------------------");
    });
}

try {
    displayUserBios(users);
} catch (error) {
    // Artıq bu hissəyə ehtiyac qalmayacaq, çünki proqram çökməyəcək
    console.error("CRITICAL ERROR: Program stopped unexpectedly!");
    console.error(error.message);
}
