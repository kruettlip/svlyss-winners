<script>
	import { Router, Route } from "svelte-navigator";
	import { MaterialApp } from "svelte-materialify";
	import NavigationBar from "./NavigationBar.svelte";
	import CurrentMonth from "./CurrentMonth.svelte";
	import MainOverview from "./MainOverview.svelte";
	import Admin from "./Admin.svelte";
	let theme = "light";

	function toggleTheme() {
		if (theme === "light") theme = "dark";
		else theme = "light";
	}
</script>

<Router primary={false}>
	<MaterialApp {theme}>
		<NavigationBar on:toggleTheme={toggleTheme} />
		<div class="main-content">
			<Route path="/">
				<CurrentMonth />
			</Route>
			<Route path="/overview">
				<MainOverview />
			</Route>
			<Route path="/admin">
				<Admin />
			</Route>
		</div>
	</MaterialApp>
</Router>

<style>
	:global(body) {
		padding: 0;
	}
	.main-content {
		padding-left: 20px;
	}
</style>
