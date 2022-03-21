function solution(genres, plays) {
    const genreTable = new Object();
    const songArray = [];
    const answer = [];
    function compareIndex(a, b) {
        return a[1] - b[1];
    }
    
    function comparePlay(a, b) {
        return b[0] - a[0];
    }
    
    function compareGenre(a, b) {
        console.log(a, b);
        return genreTable[b].play - genreTable[a].play;
    }
    
    genres.forEach((genre, index) => {
        if(genreTable.hasOwnProperty(genre)){
            genreTable[genre].play += plays[index];    
            genreTable[genre].songs.push([plays[index], index]);
        }
        else {
            genreTable[genre] = {
                play: plays[index], 
                songs: [[plays[index], index]],
            }
        }
    })
    const genreRank = Object.keys(genreTable);
    genreRank.sort(compareGenre);
    genreRank.forEach(key => {
        genreTable[key].songs.sort(compareIndex);
        genreTable[key].songs.sort(comparePlay);
        genreTable[key].songs
            .slice(0, 2)
            .forEach(([, index]) => {
                answer.push(index);
            });
    })
    
    return answer;
}