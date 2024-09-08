<script setup lang="ts">
import { useRouter } from "vue-router";
import LoginPage from "~/components/organisms/LoginPage.vue";
import { getToken, isTokenAvailable } from "~/composables/token";

async function initialize() {
  if (isTokenAvailable() && getToken()) {
    const token = getToken();
    const response = await fetch("http://localhost:8000/api/protected/", {
      method: "POST",
      headers: {
        Authorization: `Token ${token}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({}),
    });
    if (response.ok) {
      useRouter().push({ name: "home" });
    }
  }
}

onMounted(() => {
  initialize();
});
</script>

<template>
  <div class="login-page">
    <LoginPage />
  </div>
</template>

<style lang="scss" src="@/assets/styles/pages/index.scss" />
