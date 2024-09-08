<script setup lang="ts">
interface Props {
  for?: string;
  color?: "white" | "black" | "blue" | "dark-blue";
  label?: string;
}

const props = withDefaults(defineProps<Props>(), {
  color: "white",
  label: "ラベル",
});
</script>

<template>
  <label :for="`${props.for}`" :class="`label--${props.color}`">{{
    props.label
  }}</label>
</template>

<style lang="scss" src="@/assets/styles/components/atoms/label.scss" />
