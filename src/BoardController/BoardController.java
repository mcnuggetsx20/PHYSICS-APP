package BoardController;

import Entity.*;
import java.util.ArrayList;

public abstract class BoardController {
    private ArrayList<Entity> entityTable;
    private int tickRate;
    private int boardRadius = 900;
    public BoardController() {
        this.entityTable = new ArrayList<>();
    }

    public void setBoardRadius(int boardRadius) {
        this.boardRadius = boardRadius;
    }

    public int getBoardRadius() {
        return boardRadius;
    }

    public ArrayList<Entity> getEntityTable() {
        return entityTable;
    }

    public void setEntityTable(ArrayList<Entity> entityTable) {
        this.entityTable = entityTable;
    }

    public void setTickRate(int tickRate) {
        this.tickRate = tickRate;
    }

    public int getTickRate() {
        return tickRate;
    }

    public void addEntity(Entity entity) {
        entityTable.add(entity);
    }

    public void clearEntityTable(){
        ArrayList<Entity> currentEntityTable = new ArrayList<>();
        for (int i = 0; i<entityTable.size(); ++i){
            if (entityTable.get(i).getHp() > 0){
                currentEntityTable.add(entityTable.get(i));
            }
        }
        this.entityTable = currentEntityTable;
    }
}
