<template>
    <div class="container custom-container">
      <div class="text-center"><h3>User Login</h3></div>
      <!-- tab-content -->
      <form @submit.prevent="submitForm">
        <!-- Username input -->
        <div class="form-outline mb-4 mt-2">
          <label class="form-label" for="loginName">Username</label>
          <input
            type="text"
            id="loginName"
            class="form-control"
            v-model="uname"
            required
          />
        </div>
  
        <!-- Password input -->
        <div class="form-outline mb-4 mt-2">
          <label class="form-label" for="loginPassword">Password</label>
          <input
            type="password"
            id="loginPassword"
            class="form-control"
            v-model="password"
            required
          />
        </div>
  
        <!-- Login and Register button -->
        <div class="d-flex justify-content-center">
          <button type="submit" class="btn btn-primary btn-block mx-2">
            <!-- <router-link to="/adminDash" class="link-text">Login</router-link> -->
            Login
          </button>
        </div>

        <br />
        <router-link to="/user-signup" class="link-text">
          Not a user? 👉Go to Sign-Up Form
        </router-link>
      </form>
      <!-- Alert teleported on top -->
      <!-- <teleport to="#modal-root">
        <div class="container text-center">
          <div v-if="showAlert" class="alert alert-success" role="alert">
            🎉 You have successfully Signed in! Please log in to continue!
          </div>
          <div v-if="showDanger" class="alert alert-danger" role="alert">
            ⚠️ User doesn't exist, Go to Signup page !!
          </div>
          <div v-if="showDanger2" class="alert alert-danger" role="alert">
            🤔 Did you forget your password?
          </div>
        </div>
      </teleport> -->
    </div>
  </template>

<script>
export default {
  name: 'UserLogin',
  data() {
    return {
      uname: "",
      password: "",
    };
  },
  methods: {
    submitForm() {
      const user = {
        uname: this.uname,
        password: this.password,
      };
      console.log(user);
    }
  }
}
</script>

<style>
.link-text {
  color: inherit;
  text-decoration: none;
}
</style>