async function fetchAllUsers() {
    const response = await fetch('/api/user');
    const users = await response.json();
    const usersList = document.getElementById('users');
    usersList.innerHTML = '';
    users.forEach(user => {
        const li = document.createElement('li');
        li.textContent = `ID: ${user.id}, Username: ${user.username}`;
        usersList.appendChild(li);
    });
}

async function createUser() {
    const username = document.getElementById('username').value;
    const response = await fetch('/api/user', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username }),
    });

    if (response.ok) {
        alert('User created successfully');
        fetchAllUsers();
    } else {
        alert('Failed to create user');
    }
}

async function deleteUser() {
    const userId = document.getElementById('delete-user-id').value;
    const response = await fetch(`/api/user/${userId}`, {
        method: 'DELETE',
    });

    if (response.ok) {
        alert('User deleted successfully');
        fetchAllUsers();
    } else {
        alert('Failed to delete user');
    }
}

async function editUser() {
    const userId = document.getElementById('edit-user-id').value;
    const username = document.getElementById('edit-username').value;
    const response = await fetch(`/api/user/${userId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username }),
    });

    if (response.ok) {
        alert('User edited successfully');
        fetchAllUsers();
    } else {
        alert('Failed to edit user');
    }
}

async function searchUser() {
    const userId = document.getElementById('search-user-id').value;
    const response = await fetch(`/api/user/${userId}`);

    if (response.ok) {
        const user = await response.json();
        const resultDiv = document.getElementById('search-result');
        resultDiv.textContent = `ID: ${user.id}, Username: ${user.username}`;
    } else {
        alert('User not found');
    }
}

document.addEventListener('DOMContentLoaded', fetchAllUsers);
