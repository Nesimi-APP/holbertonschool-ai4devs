const users = [
    { id: 1, name: "Alice", profile: { bio: "Developer" } },
    { id: 2, name: "Bob", profile: null }, // Profile null-dur
    { id: 3, name: "Charlie" } // Profile ümumiyyətlə yoxdur
];

function displayUserBios(userList) {
    console.log("Listing User Bios...");
    
    userList.forEach(user => {
        // SƏHV: 'profile' null və ya undefined olduqda 'bio' oxuna bilmir
        // Bu proqramın çökməsinə (runtime error) səbəb olur
        const bioText = user.profile.bio; 
        
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
