<template>
    <nav class="navbar navbar-expand-lg sticky-top navbar-blurred">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">{{ name }}'s Dashboard</a>
      <div class="collapse navbar-collapse" id="navbarNav">
        <!-- <ul class="navbar-nav ms-auto">
          <li class="nav-item" v-if="isAdmin">
            <router-link to="/summary" class="nav-link">Summary</router-link>
          </li>

          <li class="nav-item" v-if="isUser">
            <router-link to="/profile" class="nav-link">Profile</router-link>
          </li>
          <li class="nav-item" v-if="isUser">
            <a class="nav-link" onclick="return false">|</a>
          </li>

          <li class="nav-item" v-if="isUser && isHome">
            <router-link to="/bookings" class="nav-link">Bookings</router-link>
          </li>
          <li class="nav-item" v-if="isUser && isBookings">
            <router-link to="/home" class="nav-link">Home</router-link>
          </li>

          <li class="nav-item">
            <a class="nav-link" onclick="return false">|</a>
          </li>
          <li class="nav-item">
            <router-link
              :to="isAdmin ? '/admin' : isUser ? '/login' : '#'"
              class="nav-link"
              >Logout</router-link
            >
          </li>
        </ul> -->
      </div>
    </div>
  </nav>
</template>

<script>
export default {
    name: 'NavBar'
}
</script>

<style>
.navbar-blurred {
  background: #9db2bf84;
  backdrop-filter: blur(4px);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
</style>