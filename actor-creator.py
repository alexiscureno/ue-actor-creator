import unreal
import sys

actors_num = int(float(sys.argv[1]))
rotation_value = int(float(sys.argv[2]))
offset_pos_value = float(sys.argv[3])


text_display = 'Spawning actors in the level'


editor_util = unreal.EditorUtilityLibrary()
selected_asset = editor_util.get_selected_assets()

with unreal.ScopedSlowTask(actors_num, text_display) as st:
    st.make_dialog(True)
    for i in range(actors_num):
        if st.should_cancel():
            break
        unreal.EditorLevelLibrary.spawn_actor_from_object(selected_asset[0],
                                                          unreal.Vector(offset_pos_value * i, offset_pos_value * i, 25.0),
                                                          unreal.Rotator(0.0, 0.0, rotation_value*i))
        unreal.log("Added a new actor in the level")
        st.enter_progress_frame(1)

