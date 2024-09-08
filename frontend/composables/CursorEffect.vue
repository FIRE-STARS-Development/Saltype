<script setup>
const cursor = ref(null);

const updateCursor = (event) => {
  if (cursor.value) {
    cursor.value.style.transform = `translate(${event.clientX}px, ${event.clientY}px)`;
  }
};

onMounted(() => {
  window.addEventListener("mousemove", updateCursor);
});

onUnmounted(() => {
  window.removeEventListener("mousemove", updateCursor);
});
</script>

<template>
  <div ref="cursor" class="cursor">
    <slot />
  </div>
</template>

<style lang="scss" src="@/assets/styles/composables/cursor-effect.scss" />
