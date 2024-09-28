<template>
    <div class="container custom-container">
      <div class="text-center"><h3>User Sign-Up</h3></div>
      <!-- tab-content -->
      <form @submit.prevent="submitForm">
        <!-- Username input -->
        <div class="form-outline mb-4 mt-2">
          <label class="form-label" for="signupName">Username</label>
          <input
            type="text"
            id="username"
            class="form-control"
            v-model="uname"
            required
          />
        </div>

        <!-- Email input -->
        <div class="form-outline mb-4 mt-2">
          <label class="form-label" for="signupName">Email</label>
          <input
            type="email"
            id="email"
            class="form-control"
            v-model="email"
            required
          />
        </div>
  
        <!-- Password input -->
        <div class="form-outline mb-4 mt-2">
          <label class="form-label" for="signupPassword">Password</label>
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
            <!-- <router-link to="/userDash" class="link-text">Login</router-link> -->
            SignUp
          </button>
        </div>

        <br />
        <router-link to="/user-login" class="link-text">
          Already a user? 👉Go to Login Form
        </router-link>
      </form>
      <!-- <teleport to="#modal-root">
        <div class="container text-center">
          <div v-if="showDanger" class="alert alert-danger" role="alert">
            ⚠️ Admin/User already exists !!
          </div>
        </div>
      </teleport> -->
    </div>
  </template>
  
  <script>
  export default {
    name: "UserSignup",
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
        console.log("Form submitted");
        console.log(user)
        // this.$router.push("/userLogin");
      },
    }
  };
  </script>
  
  <style scoped>
  .link-text {
    color: inherit;
    text-decoration: none;
  }
  </style>
  