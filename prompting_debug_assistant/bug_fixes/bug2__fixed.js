const users = [
    { id: 1, name: "Alice", profile: { bio: "Developer" } },
    { id: 2, name: "Bob", profile: null }, 
    { id: 3, name: "Charlie" } 
];

function displayUserBios(userList) {
    console.log("Listing User Bios...");
    
    userList.forEach(user => {
        // DÜZƏLİŞ: 
        // 1. user.profile?.bio -> Əgər profile null və ya undefined-dırsa, xəta vermə, undefined qaytar.
        // 2. ?? "No bio available" -> Əgər nəticə null/undefined-dırsa, bu mətni göstər.
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
    console.error("CRITICAL ERROR: Program stopped unexpectedly!");
    console.error(error.message);
}
