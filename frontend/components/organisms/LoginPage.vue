<script setup lang="ts">
import LoginForm from "../molecules/forms/LoginForm.vue";
import Title from "../atoms/texts/Title.vue";
import CursorEffect from "~/composables/CursorEffect.vue";
import GoogleAuth from "../molecules/forms/GoogleAuth.vue";
</script>

<template>
  <CursorEffect />
  <div class="login-page">
    <Title color="white" size="medium" text="ログイン" class="title" />
    <LoginForm />
    <GoogleAuth />
  </div>
</template>

<style lang="scss" src="@/assets/styles/components/organisms/login-page.scss" />
