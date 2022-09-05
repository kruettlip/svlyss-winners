import { writable, derived } from 'svelte/store';

export const apiURL = writable('http://svl.kruettlip.ch:5000/api');

function summarize(players) {
    let result = [];
    players.forEach(p => {
        const index = result.findIndex(e => e.id == p.id);
        if (index >= 0) {
            let current = result[index];
            result.splice(index, 1);
            current.points += p.points;
            result.push(current);
        } else {
            result.push(p);
        }
    });
    return result.sort((p1, p2) => {
        if (p1.points === p2.points)
            return p1.name.localeCompare(p2.name);
        return p2.points - p1.points;
    });
}

export const apiData = writable([]);
export const sessionKey = writable("");

export const firstRound = derived(apiData, ($apiData) => {
    if ($apiData.length > 0) {
        let players = $apiData.filter(m => m.monthIndex >= 8 || m.monthIndex <= 2).map(m => m.players).flat();
        return summarize(players);
    }
    return [];
});

export const secondRound = derived(apiData, ($apiData) => {
    if ($apiData.length > 0) {
        let players = $apiData.filter(m => m.monthIndex > 2 && m.monthIndex < 8).map(m => m.players).flat();
        return summarize(players);
    }
    return [];
});

export const currentMonth = derived(apiData, ($apiData) => {
    let current = $apiData.filter(m => m.monthIndex == (new Date().getMonth() + 1));
    if (current.length > 0) {
        return current[0].players.sort((p1, p2) => {
            if (p1.points === p2.points)
                return p1.name.localeCompare(p2.name);
            return p2.points - p1.points;
        });
    }
    return [];
});